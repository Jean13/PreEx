import string
import re


class parser: 

    def __init__(self, total_results, target):
        self.results = total_results
        self.target = target
        self.temp = []


    def generic_clean(self):
        self.results = re.sub('<em>', '', self.results)
        self.results = re.sub('<b>', '', self.results)
        self.results = re.sub('</b>', '', self.results)
        self.results = re.sub('</em>', '', self.results)
        self.results = re.sub('%2f', ' ', self.results)
        self.results = re.sub('%3a', ' ', self.results)
        self.results = re.sub('<strong>', '', self.results)
        self.results = re.sub('</strong>', '', self.results)
        self.results = re.sub('<wbr>', '', self.results)
        self.results = re.sub('/wbr>', '', self.results)

        for s in ('>', ':', '=', '<', '/', '\\', ';', '&', '%3A', '%3D', '%3C'):
            self.results = string.replace(self.results, s, ' ')


    def url_clean(self):
        self.results = re.sub('<em>', '', self.results)
        self.results = re.sub('</em>', '', self.results)
        self.results = re.sub('%2f', ' ', self.results)
        self.results = re.sub('%3a', ' ', self.results)

        for s in ('<', '>', ':', '=', ';', '&', '%3A', '%3D', '%3C'):
            self.results = string.replace(self.results, s, ' ')


    def emails(self):
        self.generic_clean()
        regex_emails = re.compile(
                '[a-zA-Z0-9.\-_+#~!$&\',;=:]+' +       	# username
                '@' +                                   # @ symbol
                '[a-zA-Z0-9.-]*' +                     	# domain
                self.target)
        self.temp = regex_emails.findall(self.results)
        emails = self.unique()
        return emails


    def hostnames(self):
        self.generic_clean()
        regex_hosts = re.compile('[a-zA-Z0-9.-]*\.' + self.target)
        self.temp = regex_hosts.findall(self.results)
        hostnames = self.unique()
        return hostnames


    def phone_numbers(self):
        regex_numbers = re.compile(r'''(
	(\d{3}|\(\d{3}\))?		# area code
	(\s|-|\.)?			# separator
	(\d{3})				# first 3 digits
	(\s|-|\.)			# separator
	(\d{4})				# last 4 digits
	(\s*(ext|x|ext.)\s*(\d{2,5}))?	# extension
	)''', re.VERBOSE)

	matches = []
        for groups in regex_numbers.findall(self.results):
            # Area code, first three digits, last four digits, and extension
            phoneNum = '-'.join([groups[1], groups[3], groups[5]])
            if groups[8] != '':
                phoneNum += ' x' + groups[8]
            matches.append(phoneNum)

        return matches


    def people_linkedin(self):
        regex_people = re.compile('">[a-zA-Z0-9._ -]* \| LinkedIn')
        self.temp = regex_people.findall(self.results)
        results = []
        for p in self.temp:
            y = string.replace(p, ' | LinkedIn', '')
            y = string.replace(y, ' profiles ', '')
            y = string.replace(y, 'LinkedIn', '')
            y = string.replace(y, '"', '')
            y = string.replace(y, '>', '')
            if y != " ":
                results.append(y)
        return results


    def unique(self):
        self.new = []
        for n in self.temp:
            if n not in self.new:
                self.new.append(n)
        return self.new


