import yaml
import pprint as pp
from mako.template import Template
# from tidylib import tidy_document

# pyyaml converts "yes" and "no" to "True" and "False". I don't want that.
from yaml.constructor import Constructor

def add_bool(self, node):
    return self.construct_scalar(node)

Constructor.add_constructor(u'tag:yaml.org,2002:bool', add_bool)

def main():
    inputFname = 'content.yaml'
    with open(inputFname,'r') as f:
        content = yaml.load(f)

    # pp.pprint(content)
    validate(content)
    html = htmlize(content)
    # print(html)

    with open('docs/index.html','w') as f:
        f.write(html)
    print('done')

def validate(content):
    for (i,slide) in enumerate(content):
        if 'id' not in slide:
            slide['id'] = "slide-%3d" % i
    allIDs = set([x['id'] for x in content if 'id' in x])
    for (i,slide) in enumerate(content):
        assert('id' in slide)
        for els in slide['content']:
            assert(len(els) == 1)
            assert([k for k in els.keys()][0] in ['h1','h2','p','button'])
            if 'button' in els:
                el = els['button'][0]
                # pp.pprint(el)
                if el['destination-type'].lower() == 'absolute':
                    assert(el['destination'] in allIDs)
                else:
                    assert(el['destination-type'].lower() == 'relative')
                    x = int(el['destination'])
                    assert(i+x < len(content))
                    absID = content[i+x]['id']
                    print("resolving %s + %d to %s" % (slide['id'],x,absID))
                    el['destination'] = absID
                    el['destination-type'] = 'absolute'
                assert(el['direction'] in ['left','right','up','down'])

def htmlize(content):
    with open('template.html','r') as f:
        template = Template(f.read())
    html = template.render(content=content)

    # document, errors = tidy_document(html,options={'numeric-entities':1})
    # if (errors != None) and (len(errors) > 0):
    #     pp.pprint(errors)
    #     print("Error: invalid html")
    #     # exit(1)
    #     print('continuing anyway')

    # else:
    #     print("html valid!")

    return(html)

if __name__ == '__main__':
    main()
