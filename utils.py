def get_file_extension(case):
    case = case.lower()
    if case in ["javascript", "js"]:
        return "js"
    elif case in ["python", "py"]:
        return "py"
    elif case == "java":
        return "java"
    elif case in ["c++", "cpp"]:
        return "cpp"
    elif case in ["c#", "cs"]:
        return "cs"
    elif case in ["ruby", "rb"]:
        return "rb"
    elif case in ["go", "golang"]:
        return "go"
    elif case == "rust":
        return "rs"
    elif case == "swift":
        return "swift"
    elif case == "kotlin":
        return "kt"
    elif case == "php":
        return "php"
    elif case in ["typescript", "ts"]:
        return "ts"
    elif case == "c":
        return "c"
    else:
        return "txt"
