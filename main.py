from kaggle_utils import download_and_extract_competition_files
from data_loading import JsonDataset
from torch.utils.data import DataLoader, random_split
import numpy as np
import os


if __name__ == '__main__':
    np.random.seed(0)

    if not os.path.isdir('data'):
        download_and_extract_competition_files()

    dataset = JsonDataset(
        json_directory='data/train',
        orders_filepath='data/train_orders.csv'
    )
    train_percent = 0.8
    train_size = int(len(dataset) * train_percent)
    eval_size = len(dataset) - train_size
    train_dataset, eval_dataset = random_split(dataset, [train_size, eval_size])

    train_data_loader = DataLoader(
        train_dataset,
        batch_size=32,
    )
    eval_data_loader = DataLoader(
        eval_dataset,
        batch_size=32,
    )
    for training_batch, eval_batch in zip(train_data_loader, eval_data_loader):
        print(training_batch)
        print(eval_batch)