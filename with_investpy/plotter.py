import matplotlib.pyplot as plt
import pandas as pd

STD = [0.023820889, 0.07594856, 0.13099681, 0.21202882, 0.320355046, 0.529244548, 0.903214444, 1.501874568, 3.112211651,
       1.25]
RETURN = [0.086005745, 0.840279254, 0.362646781, 0.493908207, 0.658101402, 0.636754301, 0.587396274, 0.362247124,
          0.89859536,  0.153796111]

if __name__ == '__main__':
    n = [f'D{i}' for i in range(1, 10)] + ['TA125']

    fig, ax = plt.subplots()
    ax.scatter(STD, RETURN)

    for i, txt in enumerate(n):
        ax.annotate(txt, (STD[i], RETURN[i]))
    plt.plot([0.0, 1.25 , 4], [0, 0.153796111 , (0.153796111/1.25) * 4], )
    plt.show()
