cwlVersion: v1.0
class: CommandLineTool

requirements:
  InitialWorkDirRequirement:
    listing:
      - entryname: example.sh
        entry: |-
          #!/bin/bash

          filename=`echo $(inputs.input_file.location) | awk '{ split($0,array,"://")} END{print array[2]}'`
          cat $filename | wc -w

inputs:
  input_file:
    type: File

outputs:
  output_file:
    type: File
    outputBinding:
      glob: output/output

stdout: output/output

baseCommand: ["sh", "example.sh"]