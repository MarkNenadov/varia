// Place your application-specific JavaScript functions and classes here
// This file is automatically included by javascript_include_tag :defaults

function getWordCount( text ) {
	return text.split(/\s/g).length;
}

function getLineCount( text ) {
	return text.split(/\n/g).length;
}	
