import matplotlib.pyplot as plt
def visualize_find_s_algorithm(positive_examples):
    hypothesis = ['0'] * len(positive_examples[0])
    visualization = []

    for idx, example in enumerate(positive_examples, start=1):
        for i in range(len(example)):
            if hypothesis[i] == '0':
                hypothesis[i] = example[i]
            elif hypothesis[i] != example[i]:
                hypothesis[i] = '?'
        visualization.append((idx, " ".join(hypothesis)))
    return visualization, hypothesis
positive_examples_insurance = [
    ['Middle', 'Employed', 'High', 'No', 'Healthy'],
    ['Middle', 'Employed', 'Medium', 'No', 'Healthy'],
    ['Young', 'Employed', 'High', 'No', 'Healthy']
]
visualization, final_hypothesis = visualize_find_s_algorithm(positive_examples_insurance)
plt.figure(figsize=(10,5))
plt.plot([v[0] for v in visualization], [v[1] for v in visualization], marker='o')
plt.xlabel("Example Index")
plt.ylabel("Hypothesis")
plt.title("FIND-S Algorithm – Health Insurance Eligibility")
plt.grid(True)
plt.show()
print("Final Hypothesis:", " ".join(final_hypothesis))
