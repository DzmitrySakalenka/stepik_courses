cwlVersion: v1.0
class: Workflow

requirements:
  ScatterFeatureRequirement: {}

inputs:
  input_dir: Directory

outputs:
  out_files:
    type:
      type: array
      items: File
    outputSource: cat/output_file

steps:
  get:
    run: get.cwl
    in:
      inputdir: input_dir
    out:
      [outfiles]

  cat:
    scatter: input_file
    run: cat.cwl
    in:
      input_file: get/outfiles
    out:
      [output_file]