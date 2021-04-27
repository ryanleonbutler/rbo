def get_post_content_from_file(filename):
    with open(filename) as f:
        lines = f.readlines()

    content = ""
    for line in lines:
        content += line

    return content
