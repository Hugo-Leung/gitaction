prev_tag=$1

MAIN="thesis"
latex_option="-pdf"
latexmk ${latex_option} -outdir=build ${MAIN}

if [ -n "${prev_tag}" ]; then
	latexdiff-git -r ${prev_tag} ${MAIN}.tex  --flatten
	diffName=${MAIN}-diff${prev_tag}
	echo ${diffName}
	latexmk ${latex_option} -outdir=diff ${diffName}
	mv diff/${diffName}.pdf diff/diff.pdf
fi
