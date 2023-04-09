def search_word_in_instance(word, instance, with_content=False):
    result = []
    for i in range(len(instance)):
        file = instance.search(i)
        matches = [
            {"linha": num_line+1, "conteudo": line}
            if with_content
            else {"linha": num_line+1}
            for num_line, line in enumerate(file["linhas_do_arquivo"])
            if word.lower() in line.lower()
        ]
        if matches:
            result.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": matches
            })
    return result


def exists_word(word, instance):
    return search_word_in_instance(word, instance)


def search_by_word(word, instance):
    return search_word_in_instance(word, instance, with_content=True)
