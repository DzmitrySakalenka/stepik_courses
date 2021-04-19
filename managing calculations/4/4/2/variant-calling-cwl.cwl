cwlVersion: v1.0
class: Workflow
requirements:
  - class: InlineJavascriptRequirement
  - class: StepInputExpressionRequirement
  - class: MultipleInputFeatureRequirement

inputs:
  input_bam:
    type: File

  reference_genome:
    type: File

outputs:
  reference_index:
    type: File
    outputSource: ref_ind/index

  reference_dict:
    type: File
    outputSource: ref_dic/output_dict

  bam_index:
    type: File
    outputSource: bam_ind/index

  variants_sam:
    type: File
    outputSource: var_sam/output_file

  variants_fre:
    type: File
    outputSource: var_fre/output_file

  variants_hap:
    type: File
    outputSource: var_hap/output_file

  bgz_sam:
    type: File
    outputSource: bgzip_sam/output_file

  bgz_fre:
    type: File
    outputSource: bgzip_fre/output_file  

  bgz_hap:
    type: File
    outputSource: bgzip_hap/output_file

  tab_sam:
    type: File
    outputSource: tabix_sam/output_file

  tab_fre:
    type: File
    outputSource: tabix_fre/output_file

  tab_hap:
    type: File
    outputSource: tabix_hap/output_file

  inters:
    type: File
    outputSource: intersect/output_file

  count_out:
    type: File
    outputSource: count/output_file

steps:
  ref_ind:
    run: ref_index.cwl
    in:
      reference_gen: reference_genome
    out:
      [index]

  ref_dic:
    run: ref_dict.cwl
    in:
      reference: reference_genome
    out:
      [output_dict]

  bam_ind:
    run: bam_index.cwl
    in:
      input_bam: input_bam
    out:
      [index]

  var_sam:
    run: sam_vcf.cwl
    in:
      reference_gen_for_sam: ref_ind/index
      input_bam_bai: bam_ind/index
    out:
      [output_file]

  var_fre:
    run: fre_vcf.cwl
    in:
      reference_gen_for_fre: ref_ind/index
      input_bam_bai: bam_ind/index
    out:
      [output_file]

  merge:
    run: merge.cwl
    in:
      reference_gen_for_hap: ref_ind/index
      reference_dict: ref_dic/output_dict
    out:
      [output_file]

  var_hap:
    run: hap_vcf.cwl
    in:
      reference_gen_for_hap: merge/output_file
      input_bam_bai: bam_ind/index
    out:
      [output_file]

  bgzip_sam:
    run: var_index_bgzip.cwl
    in:
      input_vcf: var_sam/output_file
    out:
      [output_file]

  tabix_sam:
    run: var_index_tabix.cwl
    in:
      input_vcf_gz: bgzip_sam/output_file
    out:
      [output_file]

  bgzip_fre:
    run: var_index_bgzip.cwl
    in:
      input_vcf: var_fre/output_file
    out:
      [output_file]

  tabix_fre:
    run: var_index_tabix.cwl
    in:
      input_vcf_gz: bgzip_fre/output_file
    out:
      [output_file]

  bgzip_hap:
    run: var_index_bgzip.cwl
    in:
      input_vcf: var_hap/output_file
    out:
      [output_file]

  tabix_hap:
    run: var_index_tabix.cwl
    in:
      input_vcf_gz: bgzip_hap/output_file
    out:
      [output_file]

  merge_sam:
    run: merge_tbi.cwl
    in:
      input_vcf_gz: bgzip_sam/output_file
      input_vcf_gz_tbi: tabix_sam/output_file
    out:
      [output_file]

  merge_fre:
    run: merge_tbi.cwl
    in:
      input_vcf_gz: bgzip_fre/output_file
      input_vcf_gz_tbi: tabix_fre/output_file
    out:
      [output_file]

  merge_hap:
    run: merge_tbi.cwl
    in:
      input_vcf_gz: bgzip_hap/output_file
      input_vcf_gz_tbi: tabix_hap/output_file
    out:
      [output_file]

  intersect:
    run: intersect.cwl
    in:
      input_sam: merge_sam/output_file
      input_fre: merge_fre/output_file
      input_hap: merge_hap/output_file
      input_bam: bam_ind/index
    out:
      [output_file]

  count:
    run: count.cwl
    in:
      input_common_var: intersect/output_file
    out:
      [output_file]
