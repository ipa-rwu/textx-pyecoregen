import argparse

from pyecoregen import cli
from .ecore import EcoreGenerator

def generate_from_cli(args):
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Generate Python classes from an Ecore model.")
    parser.add_argument(
        '--ecore-model',
        '-e',
        help="Path to Ecore XMI file.",
        required=True
    )
    parser.add_argument(
        '--out-folder',
        '-o',
        help="Path to directory, where output files are generated.",
        required=True
    )
    parser.add_argument(
        '--auto-register-package',
        help="Generate package auto-registration for the PyEcore 'global_registry'.",
        action='store_true'
    )
    parser.add_argument(
        '--user-module',
        help="Dotted name of module with user-provided mixins to import from generated classes.",
    )
    parser.add_argument(
        '--with-dependencies',
        help="Generates code for every metamodel the input metamodel depends on.",
        action='store_true'
    )
    parser.add_argument(
        '--verbose',
        '-v',
        help="Increase logging verbosity.",
        action='count'
    )

    parsed_args = parser.parse_args(args)

    cli.configure_logging(parsed_args)
    model = cli.load_model(parsed_args.ecore_model)
    EcoreGenerator(
        auto_register_package=parsed_args.auto_register_package,
        user_module=parsed_args.user_module,
        with_dependencies=parsed_args.with_dependencies
    ).generate(model, parsed_args.out_folder)


cli.generate_from_cli = generate_from_cli

def main():
    cli.main()

if __name__ == '__main__':
    main()
