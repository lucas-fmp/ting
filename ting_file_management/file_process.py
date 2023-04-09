from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file_to_enqueue = txt_importer(path_file)

    if not instance.search_file(file_to_enqueue):
        instance.enqueue(file_to_enqueue)
        print(
            {
                "nome_do_arquivo": path_file,
                "qtd_linhas": len(file_to_enqueue),
                "linhas_do_arquivo": file_to_enqueue,
            }
        )
    else:
        print(
            f"O arquivo {path_file} já existe na "
            "fila e não será adicionado novamente."
        )


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
