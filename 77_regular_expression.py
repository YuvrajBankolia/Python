import re

pattern = r"[A-Z]+arge"
text = ''' The Virgo interferometer is a was  large - scale scientific instrument near Pisa, Italy, for detecting gravitational waves. The detector measures minuscule length variations in its two 3-kilometre (1.9-mile) arms induced by the passage of gravitational waves. The project, named after the Virgo galaxy cluster, was first approved in 1992 and construction was completed in 2003. After undergoing important upgrades between 2011 and 2016 (during which LIGO made the first detection of gravitational waves), Virgo made its first detection on 14 August 2017. This was followed by the detection of GW170817, the only gravitational wave also observed with classical methods (optical, gamma-ray, X-ray and radio telescopes) as of 2024. Virgo is managed by the Virgo Collaboration, gathering 940 members in 20 countries, in cooperation with  farge similar detectors such as darge LIGO and KAGRA. (Full article...)   '''
match = re.search(pattern , text)
print(match)

# matches = re.finditer(pattern,text)
# for match in matches:
#     print(match.span())
#     # print(text[match.span()[0]:
#     # match.span()[1]])) 