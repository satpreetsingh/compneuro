import pickle
import matplotlib.pyplot as plt

with open('pop_coding.pickle', 'rb') as file:
    data = pickle.load(file)

with open('tuning.pickle', 'rb') as file:
    tuning = pickle.load(file)

v_pop = []
stim = tuning['stim']

firing_rates = {}
for neuron in ['neuron1', 'neuron2', 'neuron3', 'neuron4']:
    firing_rate = []
    for i in range(len(stim)):
        trial = []
        for values in tuning[neuron]:
            trial.append(values[i])
        firing_rate.append(sum(trial)/len(trial))

    firing_rates[neuron] = firing_rate


for i in '1234':
    r = sum(data['r'+i])/len(data['r'+i])
    r_max = max(firing_rates['neuron'+i])
    c = 90*int(i)
    v_pop.append(r/r_max)
print(v_pop)



'''
average_responses = {}
for response in ['r1', 'r2', 'r3', 'r4']:
    average_responses[response] = sum(data[response])/len(data[response])
print(average_responses)
for neuron in ['c1', 'c2', 'c3', 'c4']:
    print(data[neuron])
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
'''
