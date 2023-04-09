import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if not instance.search_file(path_file):
        file_to_enqueue = txt_importer(path_file)

        enqueue = instance.enqueue(
            {
                "nome_do_arquivo": path_file,
                "qtd_linhas": len(file_to_enqueue),
                "linhas_do_arquivo": file_to_enqueue,
            }
        )

        return print(enqueue)
    else:
        return print(
            f"O arquivo {path_file} já existe na "
            "fila e não será adicionado novamente."
        )


def remove(instance):
    dequeue = instance.dequeue()

    if dequeue is None:
        return print("Não há elementos")
    else:
        return print(
            f"Arquivo {dequeue['nome_do_arquivo']} removido com sucesso"
        )


def file_metadata(instance, position):
    try:
        data = instance.search(position)
        print(data)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
