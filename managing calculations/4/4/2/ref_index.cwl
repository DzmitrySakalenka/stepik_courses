cwlVersion: v1.0
class: CommandLineTool

requirements:
  - class: InlineJavascriptRequirement
  - class: InitialWorkDirRequirement
    listing:
    - entry: $(inputs.reference_gen)
      entryname: $(inputs.reference_gen.path.split('/').slice(-1)[0])

inputs:
  reference_gen:
    type: File
    doc: <file.fa|file.fa.gz>

outputs:
  index:
    type: File
    outputBinding:
      glob: $(inputs.reference_gen.path.split('/').slice(-1)[0])
    secondaryFiles:
      - .fai

baseCommand:
  - samtools
  - faidx

arguments:
  - valueFrom: $(inputs.reference_gen.path.split('/').slice(-1)[0])
    position: 1
