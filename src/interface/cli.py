import argparse

from src.preprocessing.preprocessing import Preprocessor
from src.calibration.calibration import Calibrator
from src.reconstruction.sfm import SfMReconstructor
from src.reconstruction.mvs import MVSReconstructor
from src.export.export import Exporter

class CLI:
    def __init__(self, config):
        self.config = config

    def run(self):
        # Set up the main parser
        parser = argparse.ArgumentParser(description="Forma CLI")
        subparsers = parser.add_subparsers(dest='command')

        # Add subcommands
        self.add_preprocess_command(subparsers)
        self.add_calibrate_command(subparsers)
        self.add_reconstruct_command(subparsers)
        self.add_export_command(subparsers)
        self.add_guidelines_command(subparsers)
        self.add_interactive_command(subparsers)

        # Parse arguments
        args = parser.parse_args()

        # Execute based on command
        if args.command == 'preprocess':
            self.preprocess(args)
        elif args.command == 'calibrate':
            self.calibrate(args)
        elif args.command == 'reconstruct':
            self.reconstruct(args)
        elif args.command == 'export':
            self.export(args)
        elif args.command == 'guidelines':
            self.guidelines()
        elif args.command == 'interactive':
            self.interactive()
        else:
            parser.print_help()

    def add_preprocess_command(self, subparsers):
        preprocess_parser = subparsers.add_parser('preprocess', help='Preprocess images')
        preprocess_parser.add_argument('--input_dir', required=True, help='Input directory of raw images')
        preprocess_parser.add_argument('--output_dir', required=True, help='Output directory for preprocessed images')

    def add_calibrate_command(self, subparsers):
        calibrate_parser = subparsers.add_parser('calibrate', help='Calibrate camera')
        calibrate_parser.add_argument('--images_dir', required=True, help='Directory of calibration images')
        calibrate_parser.add_argument('--output', required=True, help='Output file for calibration data')

    def add_reconstruct_command(self, subparsers):
        reconstruct_parser = subparsers.add_parser('reconstruct', help='Reconstruct 3D model')
        reconstruct_parser.add_argument('--images_dir', required=True, help='Directory of preprocessed images')
        reconstruct_parser.add_argument('--output_dir', required=True, help='Output directory for reconstructed model')

    def add_export_command(self, subparsers):
        export_parser = subparsers.add_parser('export', help='Export 3D model')
        export_parser.add_argument('--model_file', required=True, help='Input reconstructed model file')
        export_parser.add_argument('--format', choices=['stl', 'obj', 'ply'], required=True, help='Export format')
        export_parser.add_argument('--output_file', required=True, help='Output file for exported model')

    def add_guidelines_command(self, subparsers):
        guidelines_parser = subparsers.add_parser('guidelines', help='Display image acquisition guidelines')

    def add_interactive_command(self, subparsers):
        interactive_parser = subparsers.add_parser('interactive', help='Run in interactive mode')

    def preprocess(self, args):
        try:
            preprocessor = Preprocessor(self.config)
            preprocessor.process(args.input_dir, args.output_dir)
        except Exception as e:
            self.logger.error(f"Preprocessing failed: {e}")

    def calibrate(self, args):
        try:
            calibrator = Calibrator(self.config)
            calibrator.calibrate(args.images_dir, args.output)
        except Exception as e:
            self.logger.error(f"Calibration failed: {e}")

    def reconstruct(self, args):
        try:
            sfm = SfMReconstructor(self.config)
            sfm_result = sfm.run(args.images_dir)
            if sfm_result is None:
                raise RuntimeError("SfM reconstruction failed.")
            mvs = MVSReconstructor(self.config)
            dense_cloud = mvs.run(sfm_result)
            if dense_cloud is None:
                raise RuntimeError("MVS reconstruction failed.")
            # Save dense_cloud to args.output_dir
            # ...
        except Exception as e:
            self.logger.error(f"Reconstruction failed: {e}")

    def export(self, args):
        try:
            exporter = Exporter(self.config)
            exporter.export(args.model_file, args.format, args.output_file)
        except Exception as e:
            self.logger.error(f"Export failed: {e}")

    def guidelines(self):
        from src.acquisition.guidelines import Guidelines
        Guidelines.print_guidelines()

    def interactive(self):
        print("Entering interactive mode. Type 'help' for commands.")
        while True:
            try:
                cmd = input('> ').strip()
                if cmd == 'help':
                    print("Available commands: preprocess, calibrate, reconstruct, export, exit")
                elif cmd == 'preprocess':
                    input_dir = input('Enter input directory: ')
                    output_dir = input('Enter output directory: ')
                    self.preprocess(argparse.Namespace(input_dir=input_dir, output_dir=output_dir))
                elif cmd == 'calibrate':
                    images_dir = input('Enter calibration images directory: ')
                    output = input('Enter output file for calibration data: ')
                    self.calibrate(argparse.Namespace(images_dir=images_dir, output=output))
                elif cmd == 'reconstruct':
                    images_dir = input('Enter preprocessed images directory: ')
                    output_dir = input('Enter output directory for reconstruction: ')
                    self.reconstruct(argparse.Namespace(images_dir=images_dir, output_dir=output_dir))
                elif cmd == 'export':
                    model_file = input('Enter model file path: ')
                    file_format = input('Enter export format (stl/obj/ply): ')
                    output_file = input('Enter output file path: ')
                    self.export(argparse.Namespace(model_file=model_file, format=file_format, output_file=output_file))
                elif cmd == 'exit':
                    print("Exiting interactive mode.")
                    break
                else:
                    print("Unknown command. Type 'help' for a list of commands.")
            except KeyboardInterrupt:
                print("\nExiting interactive mode.")
                break