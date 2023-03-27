# Usage: git_controlm_api.ps1 <language> <version> <git_id>
#     Example: git_controlm_api.ps1 py “9.20.105” dcompane

# MIT License
# Copyright (c) 2021 Daniel Companeetz, BMC Software, Inc.
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# SPDX-License-Identifier: MIT
# For information on SDPX, https://spdx.org/licenses/MIT.html

#
# Comment next line if no debug information is required
Set-PSDebug -Trace 1
# Set variables from parameters
#   Language is python, go, etc. repo will use first 2 characters.
#   use java -jar swagger-codegen-cli.jar generate -l nolanguage 
#    to see the available list of languages.
#    NOTE: above command will generate an error.
$gen_language=$args[0]
$git_commit_msg=$args[1]
$git_id=$args[2]
#echo $gen_language $git_commit_msg $git_id

# Set repo name
$git_language=$gen_language.substring(0,2)
$git_repo="controlm_"+$git_language
#echo $git_repo

# MUST predownload the yaml from the EM page or other source 
#   Could use invoke-webrequest -SkipCertificateCheck -OutFile swagger-file.yaml https://<em hostname>:8443/automation-api/yaml
#     as long as certificate matching works.
#$yamlfile="swagger-file.yaml"
$yamlurl="https://vw-aus-ctm-bmc4.adprod.bmc.com:8443/automation-api/yaml"
$yamlfile="swagger-aapi.yaml"
Invoke-WebRequest -Uri $yamlurl -OutFile $yamlfile -SkipCertificateCheck


#Home dir 
if ($IsLinux) {
    $dir=$env:HOME
}
elseif ($IsMacOS) {
    $dir=$env:HOME
}
elseif ($IsWindows) {
    $dir=$env:userprofile+"\Documents"
}

#Remove prior run to avoid leave behind files.
cd $dir
#echo $dir
rd -r -fo .\$git_repo\

# Create swagger-config.json for package name and versioning
# @" is the powershell version of heredocs
(@"
{
"packageName" : "$git_repo",
"packageVersion":"$git_commit_msg"
}
"@) | set-content swagger-config.json
# Run the code.(see swagger-codegen_get.ps1 to get the jar file)
java -jar swagger-codegen-cli.jar generate `
   -i $yamlfile `
   -l $gen_language `
   -o $git_repo `
   -c swagger-config.json
   -D io.swagger.parser.util.RemoteUrl.trustAll=true   
# After generating the files, the repo directory was recreated
cd .\$git_repo\

# copy this generator to the repo
copy -path $PSCommandPath -destination .

# Add the MIT license
(@"
MIT License

Copyright (c) 2021 Daniel Companeetz, BMC Software, Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

# SPDX-License-Identifier: MIT
# For information on SDPX, https://spdx.org/licenses/MIT.html

"@) | set-content LICENSE
# Deal with the Git repo
git init
# add all files just genereted
git add .
# Define the new remote
git remote add origin https://github.com/$git_id/$git_repo.git
# Pull the prior content.
git pull origin main
# Modify the Read me for version and repo name
((Get-Content -path README.md -Raw) -creplace 'GIT_USER_ID', $git_id ) -creplace 'GIT_REPO_ID',$git_repo | Set-Content -Path README.md
git add README.md
# Modify the git_push.sh script in case someone will want to use it for version and repo name
(((Get-Content -path git_push.sh -Raw) -creplace 'GIT_USER_ID',$git_id ) -creplace 'GIT_REPO_ID',$git_repo) -creplace 'Minor update', $git_commit_msg | Set-Content -Path git_push.sh
git add git_push.sh
# Commit the newly generated files
git commit -a -m $git_commit_msg
# Change the master branch to main (master is git default, but main is github default
git branch -mv master main
# Push force to get all uploaded. Probably force is not needed, but I had to exert some authority!
git push --force origin main
# Debuggone
Set-PSDebug -Trace 0
