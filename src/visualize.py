import matplotlib.pyplot as plt

def visualize(history):

  plt.figure(figsize=(12, 4))

  plt.subplot(1,2,1) # Plot accuracy for training and validation sets
  plt.plot(history.history['accuracy'], label='Train Acc')
  plt.plot(history.history['val_accuracy'], label='Val Acc')
  plt.legend()
  plt.title('Accuracy')
  
  plt.subplot(1,2,2) # Plot loss for training and validation sets
  plt.plot(history.history['loss'], label='Train Loss')
  plt.plot(history.history['val_loss'], label='Val Loss')
  plt.legend()
  plt.title('Loss')
  plt.savefig('/output/history.png')
  plt.show()
