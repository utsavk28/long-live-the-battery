import time

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, regularizers

from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.layers import LSTM, GRU, Bidirectional
from rnn.config import *


class RNNLayers(layers.Layer):
    def __init__(self, rnn_layers_hidden_node, rnn_layer_type, is_bidirectional=False):
        super(RNNLayers, self).__init__()
        self.rnn_layers = []
        print(rnn_layer_type)

        for hidden_node in rnn_layers_hidden_node:
            if is_bidirectional:
                self.rnn_layers.append(Bidirectional(rnn_layer_type(hidden_node, activation='selu', return_sequences=True,
                                                                    kernel_regularizer=regularizers.l2(REGULARIZATION))))
            else:
                self.rnn_layers.append(rnn_layer_type(hidden_node, activation='selu', return_sequences=True,
                                                      kernel_regularizer=regularizers.l2(REGULARIZATION)))

    def call(self, input_tensor, training):
        x = None
        for layer in self.rnn_layers:
            if x is None:
                x = layer(input_tensor, training=training)
            else:
                x = layer(x, training=training)
        return x


class DenseLayers(layers.Layer):
    def __init__(self, dense_layer_hidden_nodes):
        super(DenseLayers, self).__init__()
        self.dense_layers = []
        for hidden_node in dense_layer_hidden_nodes:
            self.dense_layers.append(Dense(hidden_node, activation='selu',
                                           kernel_regularizer=regularizers.l2(REGULARIZATION)))

        self.dense_layers.append(Dense(1, activation='linear'))

    def call(self, input_tensor, training):
        x = None
        for layer in self.dense_layers:
            if x is None:
                x = layer(input_tensor, training=training)
            else:
                x = layer(x, training=training)
        return x


class RULModel(Model):
    def __init__(self, input_shape, rnn_layers_hidden_node, dense_layer_hidden_nodes, rnn_layer_type, is_bidirectional=False):
        super(RULModel, self).__init__()
        self.ip_shape = input_shape
        self.rnn = RNNLayers(rnn_layers_hidden_node,
                             rnn_layer_type, is_bidirectional)
        self.dense = DenseLayers(dense_layer_hidden_nodes)

    def call(self, input_tensor, training):
        x = self.rnn(input_tensor, training)
        x = self.dense(x, training)
        return x

    def model(self):
        x = Input(shape=self.ip_shape)
        return Model(inputs=[x], outputs=self.call(x))


def get_model(input_shape, rnn_layer='', name='', is_bidirectional=False):
    EXPERIMENT = f"{name}_rul_nasa_randomized"

    experiment_name = time.strftime("%Y-%m-%d-%H-%M-%S") + '_' + EXPERIMENT
    print(experiment_name)

    # Model definition
    opt = tf.keras.optimizers.Adam(lr=LEARNING_RATE)
    rnn_layers_hidden_node = [256, 256, 256, 128, 128, 128, 64, 64, 64]
    dense_layer_hidden_nodes = [64, 64, 32, 32]
    rnn_layer_type = LSTM if rnn_layer == 'lstm' else GRU

    model = RULModel(input_shape, rnn_layers_hidden_node,
                     dense_layer_hidden_nodes, rnn_layer_type, is_bidirectional)
    model.compile(optimizer=opt, loss='huber', metrics=[
                  'mse', 'mae', 'mape', tf.keras.metrics.RootMeanSquaredError(name='rmse')])
    model.build((1, input_shape[0], input_shape[1]))
    model.summary()
    return model, experiment_name
