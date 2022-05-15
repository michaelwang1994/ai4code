import json
import glob
import os
from torch.utils.data import Dataset
from typing import Dict, List


class JsonDataset(Dataset):
    def __init__(self, json_directory: str, orders_filepath: str):
        self.filepaths = glob.glob(f'{json_directory}/*.json')
        self.cell_orders = self._read_orders_csv(orders_filepath)

    def __getitem__(self, idx: int):
        filepath = self.filepaths[idx]
        notebook_id = os.path.basename(filepath).split('.')[0]
        notebook = json.load(open(filepath))

        # need to convert to str here because pytorch doesn't handle lists of strs
        cell_ids = str(notebook['cell_type'].keys())
        cell_types = str(notebook['cell_type'].values())
        source = str(notebook['source'].values())
        cell_order = str(self.cell_orders[notebook_id])

        return {
            'cell_ids': cell_ids,
            'cell_types': cell_types,
            'source': source,
            'orders': cell_order
        }

    def __len__(self):
        return len(self.filepaths)

    def _read_orders_csv(self, orders_filepath: str) -> Dict[str, List[str]]:
        cell_orders = {}
        with open(orders_filepath) as f:
            _ = next(f)
            for l in f:
                notebook_id, cell_order = l.split(',')
                cell_orders[notebook_id] = cell_order.split(' ')
        return cell_orders
