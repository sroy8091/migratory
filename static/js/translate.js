function googleTranslateElementInit() {
	new google.translate.TranslateElement({
		pageLanguage: 'en', 
		layout: google.translate.TranslateElement.InlineLayout.SIMPLE,
		autoDisplay: false, 
		includedLanguages: ''}, 
		'google_translate_element');
}