class: ExpressionTool
cwlVersion: v1.0

requirements:
  - class: InlineJavascriptRequirement

inputs:
  inputdir: Directory

outputs:
  outfiles: File[]

expression: |
  ${
    var samples = [];
    for (var i = 0; i < inputs.inputdir.listing.length; i++) {
      var file = inputs.inputdir.listing[i];
      if (/^\w/.test(file.basename)) {samples.push(file)};
    }
    return {"outfiles": samples};
  }