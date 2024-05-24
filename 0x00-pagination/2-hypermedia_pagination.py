#!/usr/bin/env python3
'''
Module for pagination of a database of popular baby names.
'''
import csv
from math import ceil
from typing import List


index_range = __import__('0-simple_helper_function').index_range


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        ''' Initialize instance. '''
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset

        Returns:
            List[List]: The dataset of popular baby names.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(
            self, page_number: int = 1, page_size: int = 10
            ) -> List[List]:
        """
        Return page of dataset.

        Args:
            page_number (int): The page number.
            page_size (int): The number of items per page.

        Returns:
            List[List]: The dataset page.
        """
        assert isinstance(page_number, int) and isinstance(page_size, int)
        assert page_number > 0 and page_size > 0
        indices = index_range(page_number, page_size)
        start = indices[0]
        end = indices[1]
        try:
            return self.dataset()[start:end]
        except IndexError:
            return []

    def get_hyper(self, page_number: int = 1, page_size: int = 10) -> dict:
        """
        Return dict of pagination data.

        Args:
            page_number (int): The page number.
            page_size (int): The number of items per page.

        Returns:
            dict: The pagination data,
            including page size, current page number,
            dataset page,
            next page number,
            previous page number, and total number of pages.
        """
        page_data = self.get_page(page_number, page_size)
        total_data = len(self.dataset())
        totalPages = ceil(total_data / page_size)
        return {
            'page_size': len(page_data),
            'page': page_number,
            'data': page_data,
            'next_page': page_number + 1 if page_number < totalPages else None,
            'prev_page': page_number - 1 if page_number != 1 else None,
            'total_pages': totalPages
        }
