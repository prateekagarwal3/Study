import itertools
import numpy as np
from collections import defaultdict 

def createEpsilonGreedyPolicy(Q, epsilon, num_actions): 
    def policyFunction(state): 
   
        Action_probabilities = np.ones(num_actions, 
                dtype = float) * epsilon / num_actions 
                  
        best_action = np.argmax(Q[state]) 
        Action_probabilities[best_action] += (1.0 - epsilon) 
        return Action_probabilities 
   
    return policyFunction 

def get_reward(state, action):
    state = list(state)
    state[action] = 1
    if(sum(state) == 6):
        return tuple(state), 500, 1
    else:
        return tuple(state), -5, 0

Q = defaultdict(lambda: np.zeros(6, dtype=np.float64)) 
a = [0, 1]
b = [0, 1]
c = [0, 1]
d = [0, 1]
e = [0, 1]
f = [0, 1]
states = list(itertools.product(a, b, c, d, e, f))
for s in range(len(states)):
    for a in range(6):
        Q[tuple(states[s])][a] = 0

epsilon = 0.2
gamma = 0.99
for i_episode in itertools.count():
    if(i_episode % 10 == 0):
        epsilon = epsilon * 0.98
    if(i_episode == 100):
        break
    alpha = 1/(1+i_episode)
    policy = createEpsilonGreedyPolicy(Q, epsilon, 6)
    state = tuple([0, 0, 0, 0, 0, 0])
    total_reward = 0
    for t in itertools.count():
        action_probabilities = policy(state) 
        action = np.random.choice(np.arange( 
                    len(action_probabilities)), 
                    p = action_probabilities) 

        next_state, reward, done = get_reward(state, action)
        total_reward += reward
            
        best_next_action = np.argmax(Q[next_state])     
        Q[state][action] += alpha * (reward + gamma * Q[next_state][best_next_action] - Q[state][action]) 

        if done: 
            break
        if(t == 19):
            break
        state = next_state
    print(i_episode, total_reward)