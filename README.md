# RUL-Prediction-for-Li-ion-Batteries
With its use seen in critical areas of safety and security, it is essential for lithium-ion batteries to be reliable. Prediction of the Remaining Useful Life (RUL) can give insights into the health of the battery. Variations of Recurrent Neural Networks (RNN) are employed to learn the capacity degradation trajectories of lithium-ion batteries. Using several regressor models as the baseline, an ensemble of RNNs is created to overcome the shortcomings of one RNN over the other. The critical point approach and the data-driven approach for regressor models and neural network models respectively help predict the RUL. 

## Results :
| Experiment   | Model  | Training RMSE | Testing RMSE | Validation RMSE |
| ------------ | ------ | ------------- | ------------ | --------------- |
| Experiment 1 | LSTM   | 0.0312        | 0.0304       | 0.0311          |
| BiLSTM       | 0.287  | 0.2792        | 0.3259       |
| GRU          | 0.0278 | 0.0342        | 0.0356       |
| BiGRU        | 0.0901 | 0.0945        | 0.1059       |
| Experiment 2 | LSTM   | 0.019         | 0.0173       | 0.0122          |
| BiLSTM       | 0.5521 | 0.1376        | 0.4871       |
| GRU          | 0.0962 | 0.0868        | 0.1957       |
| BiGRU        | 1.568  | 1.3482        | 1.7741       |
| Experiment 3 | LSTM   | 0.0183        | 0.0336       | 0.0542          |
| BiLSTM       | 0.107  | 0.1108        | 0.1237       |
| GRU          | 0.029  | 0.0425        | 0.0516       |
| BiGRU        | 0.034  | 0.0454        | 0.053        |
| Experiment 4 | LSTM   | 0.0248        | 0.0236       | 0.0232          |
| BiLSTM       | 0.2583 | 0.2232        | 0.1943       |
| GRU          | 0.0152 | 0.0242        | 0.0452       |
| BiGRU        | 0.2186 | 0.2282        | 0.1775       |
| Experiment 5 | LSTM   | 0.0145        | 0.0981       | 0.1329          |
| BiLSTM       | 1.2602 | 1.1037        | 0.9943       |
| GRU          | 0.0253 | 0.0811        | 0.1761       |
| BiGRU        | 0.3437 | 0.4544        | 0.4535       |
| Experiment 6 | LSTM   | 0.0123        | 0.0189       | 0.0277          |
| BiLSTM       | 0.7338 | 0.6262        | 0.6111       |
| GRU          | 0.0967 | 0.1094        | 0.2436       |
| BiGRU        | 0.138  | 0.2562        | 0.2627       |
| Experiment 7 | LSTM   | 0.0132        | 0.0253       | 0.0245          |
| BiLSTM       | 0.2486 | 0.3564        | 0.3278       |
| GRU          | 0.0578 | 0.0645        | 0.0689       |
| BiGRU        | 0.1896 | 0.2486        | 0.2156       |
| Experiment 8 | LSTM   | 0.0226        | 0.0356       | 0.0312          |
| BiLSTM       | 0.227  | 0.2792        | 0.4123       |
| GRU          | 0.0156 | 0.0236        | 0.0384       |
| BiGRU        | 0.0689 | 0.1562        | 0.1047       |
| Experiment 9 | LSTM   | 0.0196        | 0.0265       | 0.0241          |
| BiLSTM       | 0.3568 | 0.3956        | 0.4256       |
| GRU          | 0.0452 | 0.0546        | 0.0514       |
| BiGRU        | 0.0918 | 0.1256        | 0.1298       |


## Report :

## References :
### Time Series :
1. [Time Series Prediction: How Is It Different From Other Machine Learning? [ML Engineer Explains] ](https://neptune.ai/blog/time-series-prediction-vs-machine-learning)
2. [A Comprehensive Guide to Time Series Analysis](https://www.analyticsvidhya.com/blog/2021/10/a-comprehensive-guide-to-time-series-analysis/)
3. [A RoadMap to Time-Series Analysis](https://medium.com/featurepreneur/a-roadmap-for-time-series-analysis-3faf49b2126)

### Papers :
1. [Novel Statistical Analysis Approach for Remaining Useful Life Prediction of Lithium-Ion Battery](https://ieeexplore.ieee.org/document/9579982)
2. [To Charge or To Sell? EV Pack Useful Life Estimation via LSTMs and Autoencoders](https://arxiv.org/abs/2110.03585)
3. [Transformer Network for Remaining Useful Life Prediction of Lithium-Ion Batteries](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9714323)


### RUL Prediction Code :
1. [RUL Prediction for Li-ion Batteries using Critical Point](https://github.com/yash0530/RUL-Prediction-for-Li-ion-Batteries)
2. [Estimation of the Remaining Useful Life (RUL) of Lithium-ion batteries using Deep LSTMs.](https://github.com/MichaelBosello/battery-rul-estimation)
3. [Transformer Network for Remaining Useful Life Prediction of Lithium-Ion Batteries](https://github.com/XiuzeZhou/RUL)
