cwlVersion: v1.0
class: CommandLineTool
requirements:
  - class: ShellCommandRequirement
  - class: InlineJavascriptRequirement

inputs:
  input_vcf:
    type: File

outputs:
  output_file:
    type: stdout

baseCommand: []

arguments:
  - bgzip
  - -c
  - $(inputs.input_vcf)

stdout: $(inputs.input_vcf.basename+".gz")
