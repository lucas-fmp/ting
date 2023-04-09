def exists_word(word, instance):
    result = []
    for i in range(len(instance)):
        file = instance.search(i)
        lines = []
        for num_line, line in enumerate(file["linhas_do_arquivo"], start=1):
            if word.lower() in line.lower():
                lines.append({"linha": num_line})
        if lines:
            result.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": lines
                })
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
