from argparse import ArgumentParser


def get_arguments():
    parser = ArgumentParser(description='Sample Flask Application')

    parser.add_argument('-e', '--environment', type=str,
                        default="dev", choices=["dev", "stg", "prod"])
    parser.add_argument('-p', '--port', type=int,
                        choices=range(1024, 49150), default=5000)

    return parser.parse_args()
