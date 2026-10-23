name: Compile OBJ to Game BIN

on:
  workflow_dispatch:
    inputs:
      obj_filename:
        description: 'Type the exact name of the .obj file in the repo root (e.g. knux.obj)'
        required: true
        default: 'knux.obj'
        type: string

jobs:
  convert_to_bin:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository Code
        uses: actions/checkout@v4

      - name: Set Up Python Environment
        uses: actions/setup-python@v5
        with:
          python-version: '3.x'

      - name: Run obj2srm Converter
        run: |
          # Dynamically extracts the base name and runs the utility script
          FILENAME="${{ inputs.obj_filename }}"
          BASENAME="${FILENAME%.*}"
          python3 charmodel-utils/obj2srm.py "$FILENAME" "${BASENAME}.bin"

      - name: Upload Compiled Binary Asset
        uses: actions/upload-artifact@v4
        with:
          name: compiled-game-binaries
          path: "*.bin"
