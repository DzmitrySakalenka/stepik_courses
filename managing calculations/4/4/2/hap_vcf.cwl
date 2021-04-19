cwlVersion: v1.0
class: CommandLineTool
requirements:
  - class: ShellCommandRequirement
  - class: InlineJavascriptRequirement

inputs:
  reference_gen_for_hap:
    type: File
    secondaryFiles:
      - .fai
      - ^.dict

  input_bam_bai:
    type: File
    secondaryFiles:
      - .bai

outputs:
  output_file:
    type: File
    outputBinding:
      glob: $(inputs.input_bam_bai.nameroot + "_hap.vcf")

baseCommand: []

arguments:
  - java
  - -jar
  - /opt/gatk/GenomeAnalysisTK.jar
  - -R
  - $(inputs.reference_gen_for_hap)
  - -T
  - HaplotypeCaller
  - -I
  - $(inputs.input_bam_bai)
  - -o
  - $(inputs.input_bam_bai.nameroot + "_hap.vcf")
