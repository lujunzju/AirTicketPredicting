
import numpy as np
import matplotlib.pyplot as plt


sgd = [[  1, 0.31075, 0.22447, 1.3398,  0.06],
 [  2, 0.2311,  0.21895, 1.0098,  0.03],
 [  3, 0.22895, 0.21607, 1.01334, 0.05],
 [  4, 0.22912, 0.21563, 1.01618, 0.05],
 [  5, 0.22692, 0.21437, 1.01191, 0.04],
 [  6, 0.22695, 0.21381, 1.01469, 0.03],
 [  7, 0.22576, 0.21235, 1.01605, 0.03],
 [  8, 0.22495, 0.21194, 1.0142,  0.03],
 [  9, 0.22449, 0.21679, 0.98941, 0.03],
 [ 10, 0.22361, 0.21044, 1.01507, 0.03],
 [ 11, 0.22305, 0.21243, 1.00294, 0.03],
 [ 12, 0.22217, 0.21031, 1.00885, 0.03],
 [ 13, 0.22178, 0.21151, 1.00131, 0.03],
 [ 14, 0.22156, 0.21161, 0.9998,  0.03],
 [ 15, 0.221,   0.20782, 1.01527, 0.03],
 [ 16, 0.21988, 0.2152,  0.97528, 0.03],
 [ 17, 0.21995, 0.20848, 1.00706, 0.03],
 [ 18, 0.21915, 0.21153, 0.98877, 0.03],
 [ 19, 0.21889, 0.20807, 1.00396, 0.03],
 [ 20, 0.21777, 0.21213, 0.97943, 0.03],
 [ 21, 0.21796, 0.20912, 0.99444, 0.03],
 [ 22, 0.21693, 0.21145, 0.97863, 0.03],
 [ 23, 0.21659, 0.2067,  0.99948, 0.03],
 [ 24, 0.21647, 0.21167, 0.9754,  0.04],
 [ 25, 0.21631, 0.2071,  0.99616, 0.03]]


momentum=[[ 1,0.40577,0.24340,1.66712  ,0.04],
[ 2,0.22425,0.22293,1.00594  ,0.04],
[ 3,0.22247,0.22515,0.98809  ,0.04],
[ 4,0.22224,0.22889,0.97095  ,0.03],
[ 5,0.22171,0.22406,0.98950  ,0.03],
[ 6,0.22143,0.22238,0.99573  ,0.04],
[ 7,0.22157,0.22228,0.99683  ,0.04],
[ 8,0.22050,0.22111,0.99725  ,0.04],
[ 9,0.22047,0.21883,1.00748  ,0.04],
[10,0.22019,0.22039,0.99909  ,0.03],
[11,0.21969,0.21686,1.01306  ,0.04],
[12,0.21854,0.21576,1.01289  ,0.04],
[13,0.21891,0.21732,1.00733  ,0.04],
[14,0.21855,0.21619,1.01091  ,0.04],
[15,0.21796,0.21833,0.99830  ,0.04],
[16,0.21752,0.21454,1.01390  ,0.04],
[17,0.21503,0.21109,1.01870  ,0.03],
[18,0.21652,0.21335,1.01489  ,0.04],
[19,0.21684,0.21338,1.01621  ,0.04],
[20,0.21723,0.22440,0.96803  ,0.04],
[21,0.21528,0.21163,1.01727  ,0.04],
[22,0.21125,0.21120,1.00024  ,0.03],
[23,0.21314,0.20939,1.01789  ,0.03],
[24,0.21267,0.21202,1.00307  ,0.04],
[25,0.21096,0.21067,1.00137  ,0.04]]


nexterov = [[  1,0.41896],
[  2,0.22903],
[  3,0.22116],
[  4,0.21722],
[  5,0.21623],
[  6,0.21527],
[  7,0.21270],
[  8,0.21063],
[  9,0.21231],
[ 10,0.22115],
[ 11,0.21327],
[ 12,0.21774],
[ 13,0.21669],
[ 14,0.21607],
[ 15,0.21559],
[ 16,0.21506],
[ 17,0.21411],
[ 18,0.20993],
[ 19,0.21372],
[ 20,0.21269],
[ 21,0.21169],
[ 22,0.20656],
[ 23,0.20959],
[ 24,0.20774],
[ 25,0.20279]]

nexterov = np.array(nexterov)
momentum = np.array(momentum)
sgd = np.array(sgd)


plt.plot(nexterov[:,0],1.0 - nexterov[:,1], 'o-', color="r",
                 label="Nesterov momentum")
plt.plot(momentum[:,0],1.0 - momentum[:,1], '*-', color="g",
                 label="momentum")
plt.plot(sgd[:,0],1.0 - sgd[:,1], 's-', color="b",
                 label="sgd")

plt.legend(loc="best")

plt.xlabel('Number of epochs')
plt.ylabel('Accuracy (1 - error rate)')
plt.title('Effect of update methods')
plt.grid(True)
plt.savefig("nnupdate.pdf")
plt.show()

