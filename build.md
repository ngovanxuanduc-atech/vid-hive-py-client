# Build Instructions for Vid Hive Python Client

To build the `vid-hive-py-client` package, follow these steps:

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can check this by running `python --version` or `python3 --version` in your terminal.

2. **Navigate to the Project Directory**: Open a terminal and navigate to the `vid-hive-py-client` directory:

   ```bash
   cd c:\source_atech\vid-hive\vid-hive-py-client
   ```

3. **Install Build Tools**: Ensure you have the necessary tools to build the package. You can install them using pip:

   ```bash
   pip install setuptools wheel
   ```

4. **Build the Package**: Run the following command to build the package:

   ```bash
   python setup.py sdist bdist_wheel
   ```

   This will create a `dist/` directory containing the built package files.

5. **Verify the Build**: Check the `dist/` directory for the generated `.tar.gz` and `.whl` files.

6. **Install the Package Locally (Optional)**: If you want to test the package locally, you can install it using pip:
   ```bash
   pip install dist/vid_hive_client-<version>.whl
   ```
   Replace `<version>` with the actual version number of the package.
