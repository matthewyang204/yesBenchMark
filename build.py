import subprocess
import sys
import os

version_msg = """matthewyang204's Python Build Engine for yesBenchMark, version 0.0.0
(C) Matthew Yang 2025-2026"""

help_msg = f"""Usage: {sys.executable} build.py [options]

Options:
  --help, -h          Show this help message & exit
  --version, -v       Print version info & exit
  --install-deps      Only install dependencies & exit without building"""

def install_deps(build=False):
    os.system(f"{sys.executable} -m pip install -r requirements.txt")
    if build:
        os.system(f"{sys.executable} -m pip install -r requirements-build.txt")

def run_pyinstaller():
    try:
        main_script = os.path.join('yesbenchmark', 'main.py')

        cmd = [
            'pyinstaller',
            main_script,
            '--onefile',
            '--name', 'yesbenchmark'
        ]

        # Run PyInstaller
        subprocess.check_call(cmd)

        print("Build successful.")
    except Exception as e:
        print(f"Build failed: {e}")

def main():
    global version_msg, help_msg
    args = sys.argv
    
    if '--help' in args or '-h' in args:
        print(help_msg)
        sys.exit()
    elif '--version' in args or '-v' in args:
        print(version_msg)
        sys.exit()
    elif '--install-deps' in args:
        print("Installing dependencies for yesbenchmark...")
        install_deps()
        sys.exit()

    print("Installing dependencies before build...")
    install_deps(build=True)
    print("Building...")
    run_pyinstaller()
    print("done")

if __name__ == '__main__':
    main()