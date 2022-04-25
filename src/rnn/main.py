from sklearn.model_selection import train_test_split
import pandas as pd
from rnn.config import *
from src.config import *
from model import get_model
import tensorflow as tf
from preprocess import get_exp_based_df

if __name__ == "__main__":
    # experiment1, experiment2, experiment3, experiment4, experiment5, experiment6, experiment7, experiment8, experiment9
    df_x, df_y = get_exp_based_df(experiment1)
    train_x, test_x, train_y, test_y = train_test_split(
        df_x, df_y, test_size=0.2, random_state=0)
    test_x, val_x, test_y, val_y = train_test_split(
        test_x, test_y, test_size=0.5, random_state=0)

    input_shape = (train_x.shape[1], train_x.shape[2])
    model, experiment_name = get_model(input_shape, rnn_layer='gru',
                                       name='gru', is_bidirectional=False)

    data_path = "./model"
    if IS_TRAINING:
        def scheduler(epoch, lr):
            if epoch < 10:
                return lr+STEP_LR
            elif epoch % 5 == 0:
                return lr*0.99
            return lr

        early_stopping = tf.keras.callbacks.EarlyStopping(
            monitor='loss', patience=EARLY_STOPPING)
        lr_scheduler = tf.keras.callbacks.LearningRateScheduler(scheduler)

        history = model.fit(train_x, train_y, epochs=NUM_EPOCHS, batch_size=BATCH_SIZE,
                            verbose=1, validation_split=0.1, callbacks=[early_stopping, lr_scheduler])

        model.save(data_path + '../../output/results/trained_model/%s.h5' %
                   experiment_name)

        hist_df = pd.DataFrame(history.history)
        hist_csv_file = data_path + \
            '../../output/results/trained_model/%s_history.csv' % experiment_name
        with open(hist_csv_file, mode='w') as f:
            hist_df.to_csv(f)
        history = history.history

    model.evaluate(train_x, train_y)
    model.evaluate(val_x, val_y)
    model.evaluate(test_x, test_y)
