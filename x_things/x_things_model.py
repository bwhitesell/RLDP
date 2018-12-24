from torch import nn


class XThingsModel(nn.Module):
    def __init__(self, input_count: int, output_count: int):
        super().__init__()
        self.input_count = input_count
        self.layers = nn.Sequential(
            nn.Linear(input_count, 512),
            nn.Dropout(p=0.5),
            nn.ReLU(),
            nn.Linear(512, 128),
            nn.ReLU(),
            nn.Linear(128, output_count),
            nn.Sigmoid()
        )

    def forward(self, game_state):
        return self.layers(game_state)

