cwlVersion: v1.0
class: CommandLineTool

requirements:
  - class: InlineJavascriptRequirement

inputs:
  reference:
    type: File
    doc: |
      Input reference fasta or fasta.gz

outputs:
  output_dict:
    type: File
    outputBinding:
      glob: $(inputs.reference.nameroot).dict

baseCommand: []
arguments:
  - java
  - -jar
  - /opt/picard/picard.jar
  - CreateSequenceDictionary
  - 'R='
  - $(inputs.reference)
  - 'O='
  - $(inputs.reference.nameroot).dict
