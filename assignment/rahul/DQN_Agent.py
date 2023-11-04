import random
import gym
import torch
import torch.nn as nn
import torch.optim as optim
from collections import deque
import os

torch.manual_seed(42)
random.seed(42)

class PolicyModel(nn.Module):
    def __init__(self, state_size, action_size, learning_rate):
        super(PolicyModel, self).__init__()

        self.fc1 = nn.Linear(state_size, 24)
        self.fc2 = nn.Linear(24, 24)
        self.fc3 = nn.Linear(24, action_size)

        self.relu = nn.ReLU()

        self.optimizer = optim.Adam(self.parameters(), lr=learning_rate)
        self.criterion = nn.MSELoss()

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.fc3(x)
        return x

    def fit(self, state, target_f):
        self.train()

        state_tensor = torch.tensor(state, dtype=torch.float32)
        target_f_tensor = torch.tensor(target_f, dtype=torch.float32)

        self.optimizer.zero_grad()

        output = self(state_tensor)

        loss = self.criterion(output, target_f_tensor)
        loss.backward()
        self.optimizer.step()

        return loss.item()


class DQNAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size

        self.memory = deque(maxlen=10000)
        self.gamma = 0.95
        self.epsilon = 1.0
        self.epsilon_decay = 0.995
        self.epsilon_min = 0.01
        self.learning_rate = 0.001
        self.model = PolicyModel(self.state_size, self.action_size, self.learning_rate)

    def remember(self, state, action, reward, next_state, done):
        self.memory.append([state, action, reward, next_state, done])

    def act(self, state, train=True):
        if random.random() <= self.epsilon and train:
            return random.randrange(self.action_size)
        else:
            self.model.eval()
            state_tensor = torch.tensor(state, dtype=torch.float32)
            act_values = self.model(state_tensor)
            return torch.argmax(act_values).item()

    def replay(self, batch_size):
        self.model.eval()
        minibatch = random.sample(self.memory, batch_size)

        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                next_state_tensor = torch.tensor(next_state, dtype=torch.float32)
                target = reward + self.gamma * torch.max(self.model(next_state_tensor)).item()

            state_tensor = torch.tensor(state, dtype=torch.float32)
            target_f = self.model(state_tensor).clone()
            target_f[0][action] = target

            self.model.fit(state, target_f)

        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def load(self, name):
        self.model.load_state_dict(torch.load(name))

    def save(self, name):
        torch.save(self.model.state_dict(), name)
        
    def punish_last(self, num):
        for i in range(1, 1+num):
            self.memory[-i][2] = -10/i