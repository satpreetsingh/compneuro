import pickle
import matplotlib.pyplot as plt

with open('tuning.pickle', 'rb') as file:
    data = pickle.load(file)

for neuron in ['neuron1', 'neuron2', 'neuron3', 'neuron4']:
    firing_rate = []
    for i in range(len(data['stim'])):
        trial = []
        for values in data[neuron]:
            trial.append(values[i])
        firing_rate.append(sum(trial)/len(trial))

    print(data['stim'])
    print(firing_rate)
    plt.plot(data['stim'], firing_rate, label=neuron)

plt.legend()
plt.xlabel('stimulus (degrees)')
plt.ylabel('firing rate (Hz)')
plt.show()
