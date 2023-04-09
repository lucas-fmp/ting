import pytest
from ting_file_management.priority_queue import PriorityQueue

input_1 = {
    "nome_do_arquivo": "input_1",
    "qtd_linhas": 7,
    "linhas_do_arquivo": ["1", "2", "3", "4", "5", "6", "7"],
}

input_2 = {
    "nome_do_arquivo": "input_2",
    "qtd_linhas": 8,
    "linhas_do_arquivo": ["1", "2", "3", "4", "5", "6", "7", "8"],
}

input_3 = {
    "nome_do_arquivo": "input_3",
    "qtd_linhas": 4,
    "linhas_do_arquivo": ["1", "2", "3", "4"],
}

input_4 = {
    "nome_do_arquivo": "input_4",
    "qtd_linhas": 6,
    "linhas_do_arquivo": ["1", "2", "3", "4", "5", "6"],
}

input_5 = {
    "nome_do_arquivo": "input_5",
    "qtd_linhas": 3,
    "linhas_do_arquivo": ["1", "2", "3"],
}


def test_basic_priority_queueing():
    pq = PriorityQueue()

    pq.enqueue(input_1)
    pq.enqueue(input_2)
    pq.enqueue(input_3)
    pq.enqueue(input_4)
    pq.enqueue(input_5)

    given = pq.dequeue()
    assert given == input_3

    assert pq.search(0) == input_5

    with pytest.raises(IndexError):
        pq.search(-1)
