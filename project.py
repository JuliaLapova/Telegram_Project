import torch
from torchvision import datasets, transforms
import torchvision
import numpy as np
import matplotlib.pyplot as plt
from torch.utils.tensorboard import SummaryWriter

# Настройка трансформаций
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

# Загрузка датасета MNIST
train_dataset = datasets.MNIST(root='data', train=True, download=True, transform=transform)
train_loader = torch.utils.data.DataLoader(dataset=train_dataset, batch_size=64, shuffle=True)

# Визуализация нескольких изображений
def imshow(img):
    img = img / 2 + 0.5  # Денормализация
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0)), cmap='gray')
    plt.show()

# Получение одной партии данных
dataiter = iter(train_loader)
images, labels = next(dataiter)

# Отображение первых 4 изображений
imshow(torchvision.utils.make_grid(images[:4]))
print('GroundTruth: ', ' '.join(str(labels[j].item()) for j in range(4)))

# Запуск TensorBoard
writer = SummaryWriter('runs/test_run')
writer.add_images('mnist_images', images[:4], 0)
writer.close()