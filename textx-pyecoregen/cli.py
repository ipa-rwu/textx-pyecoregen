from pyecoregen import cli
from ecore import EcoreGenerator

def _createGenerator(parsed_args):
    return EcoreGenerator(
        auto_register_package=parsed_args.auto_register_package,
        user_module=parsed_args.user_module,
        with_dependencies=parsed_args.with_dependencies
    )

cli._createGenerator = _createGenerator

if __name__ == '__main__':  # nocover
    cli.main()
