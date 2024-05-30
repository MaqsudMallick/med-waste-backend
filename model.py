from torchvision import transforms, models
import torch.nn as nn
import torch
import torch.optim as optim
from PIL import Image

class ConvNext(nn.Module):
    def __init__(self):
        super(ConvNext, self).__init__()
        self.convnext = models.convnext_base(pretrained=True)
        self.fc = nn.Linear(1000, 4)

    def forward(self, x):
        out = self.convnext(x)
        out = self.fc(out)
        return out
    
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = ConvNext()
model.load_state_dict(torch.load('ConvNext_modelmedicalwaste.pt', map_location=torch.device('cpu')))
model.to(device)

preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

def get_class(input_image):

    # input_image = Image.open(path).convert('RGB')

    # Preprocess the image
    input_tensor = preprocess(input_image)
    input_batch = input_tensor.unsqueeze(0)  # Create a mini-batch as expected by the model

    # Move the input to the appropriate device
    input_batch = input_batch.to(device)

    # Pass the image through the model
    with torch.no_grad():
        output = model(input_batch)

    _, predicted = torch.max(output, 1)
    print(f'Predicted class: {predicted.item()}')
    return predicted.item()




