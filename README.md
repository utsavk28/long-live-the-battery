# RUL-Prediction-for-Li-ion-Batteries
With its use seen in critical areas of safety and security, it is essential for lithium-ion batteries to be reliable. Prediction of the Remaining Useful Life (RUL) can give insights into the health of the battery. Variations of Recurrent Neural Networks (RNN) are employed to learn the capacity degradation trajectories of lithium-ion batteries. Using several regressor models as the baseline, an ensemble of RNNs is created to overcome the shortcomings of one RNN over the other. The critical point approach and the data-driven approach for regressor models and neural network models respectively help predict the RUL. 


## Report 
[Project Report](https://github.com/utsavk28/RUL-Prediction-for-Li-ion-Batteries/blob/main/Project_Report.pdf)

## Results 

### Various RNN Model Results 

<table class="tableizer-table">
<thead><tr class="tableizer-firstrow"><th>Experiment</th><th>Model</th><th>Training RMSE</th><th>Testing RMSE</th><th>Validation RMSE</th></tr></thead><tbody>
 <tr><td>Experiment 1</td><td>LSTM</td><td>0.0312</td><td>0.0304</td><td>0.0311</td></tr>
 <tr><td>&nbsp;</td><td>BiLSTM</td><td>0.287</td><td>0.2792</td><td>0.3259</td></tr>
 <tr><td>&nbsp;</td><td>GRU</td><td>0.0278</td><td>0.0342</td><td>0.0356</td></tr>
 <tr><td>&nbsp;</td><td>BiGRU</td><td>0.0901</td><td>0.0945</td><td>0.1059</td></tr>
 <tr><td>Experiment 2</td><td>LSTM</td><td>0.019</td><td>0.0173</td><td>0.0122</td></tr>
 <tr><td>&nbsp;</td><td>BiLSTM</td><td>0.5521</td><td>0.1376</td><td>0.4871</td></tr>
 <tr><td>&nbsp;</td><td>GRU</td><td>0.0962</td><td>0.0868</td><td>0.1957</td></tr>
 <tr><td>&nbsp;</td><td>BiGRU</td><td>1.568</td><td>1.3482</td><td>1.7741</td></tr>
 <tr><td>Experiment 3</td><td>LSTM</td><td>0.0183</td><td>0.0336</td><td>0.0542</td></tr>
 <tr><td>&nbsp;</td><td>BiLSTM</td><td>0.107</td><td>0.1108</td><td>0.1237</td></tr>
 <tr><td>&nbsp;</td><td>GRU</td><td>0.029</td><td>0.0425</td><td>0.0516</td></tr>
 <tr><td>&nbsp;</td><td>BiGRU</td><td>0.034</td><td>0.0454</td><td>0.053</td></tr>
 <tr><td>Experiment 4</td><td>LSTM</td><td>0.0248</td><td>0.0236</td><td>0.0232</td></tr>
 <tr><td>&nbsp;</td><td>BiLSTM</td><td>0.2583</td><td>0.2232</td><td>0.1943</td></tr>
 <tr><td>&nbsp;</td><td>GRU</td><td>0.0152</td><td>0.0242</td><td>0.0452</td></tr>
 <tr><td>&nbsp;</td><td>BiGRU</td><td>0.2186</td><td>0.2282</td><td>0.1775</td></tr>
 <tr><td>Experiment 5</td><td>LSTM</td><td>0.0145</td><td>0.0981</td><td>0.1329</td></tr>
 <tr><td>&nbsp;</td><td>BiLSTM</td><td>1.2602</td><td>1.1037</td><td>0.9943</td></tr>
 <tr><td>&nbsp;</td><td>GRU</td><td>0.0253</td><td>0.0811</td><td>0.1761</td></tr>
 <tr><td>&nbsp;</td><td>BiGRU</td><td>0.3437</td><td>0.4544</td><td>0.4535</td></tr>
 <tr><td>Experiment 6</td><td>LSTM</td><td>0.0123</td><td>0.0189</td><td>0.0277</td></tr>
 <tr><td>&nbsp;</td><td>BiLSTM</td><td>0.7338</td><td>0.6262</td><td>0.6111</td></tr>
 <tr><td>&nbsp;</td><td>GRU</td><td>0.0967</td><td>0.1094</td><td>0.2436</td></tr>
 <tr><td>&nbsp;</td><td>BiGRU</td><td>0.138</td><td>0.2562</td><td>0.2627</td></tr>
 <tr><td>Experiment 7</td><td>LSTM</td><td>0.0132</td><td>0.0253</td><td>0.0245</td></tr>
 <tr><td>&nbsp;</td><td>BiLSTM</td><td>0.2486</td><td>0.3564</td><td>0.3278</td></tr>
 <tr><td>&nbsp;</td><td>GRU</td><td>0.0578</td><td>0.0645</td><td>0.0689</td></tr>
 <tr><td>&nbsp;</td><td>BiGRU</td><td>0.1896</td><td>0.2486</td><td>0.2156</td></tr>
 <tr><td>Experiment 8</td><td>LSTM</td><td>0.0226</td><td>0.0356</td><td>0.0312</td></tr>
 <tr><td>&nbsp;</td><td>BiLSTM</td><td>0.227</td><td>0.2792</td><td>0.4123</td></tr>
 <tr><td>&nbsp;</td><td>GRU</td><td>0.0156</td><td>0.0236</td><td>0.0384</td></tr>
 <tr><td>&nbsp;</td><td>BiGRU</td><td>0.0689</td><td>0.1562</td><td>0.1047</td></tr>
 <tr><td>Experiment 9</td><td>LSTM</td><td>0.0196</td><td>0.0265</td><td>0.0241</td></tr>
 <tr><td>&nbsp;</td><td>BiLSTM</td><td>0.3568</td><td>0.3956</td><td>0.4256</td></tr>
 <tr><td>&nbsp;</td><td>GRU</td><td>0.0452</td><td>0.0546</td><td>0.0514</td></tr>
 <tr><td>&nbsp;</td><td>BiGRU</td><td>0.0918</td><td>0.1256</td><td>0.1298</td></tr>
</tbody></table>

### Ensembling Results 

<table class="tableizer-table">
<thead><tr class="tableizer-firstrow"><th>Experiment</th><th>Model</th><th>Train RMSE</th><th>Validation RMSE</th><th>Test RMSE</th></tr></thead><tbody>
 <tr><td>Experiment 1</td><td>Experiment1_CatBoostRegressor</td><td>0.007525</td><td>0.027265</td><td>0.020191</td></tr>
 <tr><td>&nbsp;</td><td>Experiment1_ExtraTreesRegressor</td><td>2.05E-15</td><td>0.032114</td><td>0.019708</td></tr>
 <tr><td>&nbsp;</td><td>Experiment 2_LGBMRegressor</td><td>0.015742</td><td>0.01869</td><td>0.121217</td></tr>
 <tr><td>Experiment 2</td><td>Experiment 2_RandomForestRegressor</td><td>0.008446</td><td>0.016777</td><td>0.118291</td></tr>
 <tr><td>Experiment 3</td><td>Experiment 3_ExtraTreesRegressor</td><td>1.97E-15</td><td>0.027225</td><td>0.050309</td></tr>
 <tr><td>&nbsp;</td><td>Experiment 3_XGBRegressor</td><td>0.001102</td><td>0.032008</td><td>0.052786</td></tr>
 <tr><td>Experiment 4</td><td>Experiment 4_ExtraTreeRegressor</td><td>0</td><td>0.038955</td><td>0.096077</td></tr>
 <tr><td>&nbsp;</td><td>Experiment 4_LGBMRegressor</td><td>0.064483</td><td>0.076645</td><td>0.094264</td></tr>
 <tr><td>Experiment 5</td><td>Experiment 5_DecisionTreeRegressor</td><td>0</td><td>0.036995</td><td>0.027503</td></tr>
 <tr><td>&nbsp;</td><td>Experiment 5_RandomForestRegressor</td><td>0.023868</td><td>0.033271</td><td>0.033192</td></tr>
 <tr><td>Experiment 6</td><td>Experiment 6_HuberRegressor</td><td>0.012126</td><td>0.018583</td><td>0.020066</td></tr>
 <tr><td>&nbsp;</td><td>Experiment 6_LinearRegression</td><td>0.01206</td><td>0.018489</td><td>0.019934</td></tr>
 <tr><td>Experiment 7</td><td>Experiment 7_HuberRegressor</td><td>0.015001</td><td>0.026221</td><td>0.013487</td></tr>
 <tr><td>&nbsp;</td><td>Experiment 7_LinearRegression</td><td>0.014968</td><td>0.026394</td><td>0.013531</td></tr>
 <tr><td>&nbsp;</td><td>Experiment 7_LinearSVR</td><td>0.016352</td><td>0.029895</td><td>0.01475</td></tr>
 <tr><td>Experiment 8</td><td>Experiment 8_DecisionTreeRegressor</td><td>0</td><td>0.075652</td><td>0.339136</td></tr>
 <tr><td>&nbsp;</td><td>Experiment 8_LinearSVR</td><td>0.042245</td><td>0.108166</td><td>0.342323</td></tr>
 <tr><td>Experiment 9</td><td>Experiment 9_CatBoostRegressor</td><td>0.006819</td><td>0.043317</td><td>0.031779</td></tr>
 <tr><td>&nbsp;</td><td>Experiment 9_ExtraTreesRegressor</td><td>1.59E-15</td><td>0.039875</td><td>0.031513</td></tr>
 <tr><td>&nbsp;</td><td>Experiment 9_LGBMRegressor</td><td>0.04493</td><td>0.124974</td><td>0.031858</td></tr>
</tbody></table>


## References 
### Time Series 
1. [Time Series Prediction: How Is It Different From Other Machine Learning? [ML Engineer Explains] ](https://neptune.ai/blog/time-series-prediction-vs-machine-learning)
2. [A Comprehensive Guide to Time Series Analysis](https://www.analyticsvidhya.com/blog/2021/10/a-comprehensive-guide-to-time-series-analysis/)
3. [A RoadMap to Time-Series Analysis](https://medium.com/featurepreneur/a-roadmap-for-time-series-analysis-3faf49b2126)

### Papers 
1. [Novel Statistical Analysis Approach for Remaining Useful Life Prediction of Lithium-Ion Battery](https://ieeexplore.ieee.org/document/9579982)
2. [To Charge or To Sell? EV Pack Useful Life Estimation via LSTMs and Autoencoders](https://arxiv.org/abs/2110.03585)
3. [Transformer Network for Remaining Useful Life Prediction of Lithium-Ion Batteries](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9714323)


### RUL Prediction Code 
1. [RUL Prediction for Li-ion Batteries using Critical Point](https://github.com/yash0530/RUL-Prediction-for-Li-ion-Batteries)
2. [Estimation of the Remaining Useful Life (RUL) of Lithium-ion batteries using Deep LSTMs.](https://github.com/MichaelBosello/battery-rul-estimation)
3. [Transformer Network for Remaining Useful Life Prediction of Lithium-Ion Batteries](https://github.com/XiuzeZhou/RUL)
