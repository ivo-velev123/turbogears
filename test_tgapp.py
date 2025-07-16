import kajiki


def test_index_template():
    with open("index.xhtml", "r") as f:
        lines = f.readlines()

    output = "".join(lines)

    template = kajiki.XMLTemplate(output)
    print(template(dict(person="ivo")).render())
    comparison = "".join(template(dict(person="ivo")).render())

    assert """<html>
    <body>
        <header>
            
                <h1>ivo's HTML Website practice</h1>
            
        </header>
        <article>
            <h3 class="left">Here is a list of things you can do with HTML5:</h3>
            <ul class="left">
                <li><a href="html5Elements.html">These are a few elements.</a></li>
                <li><a href="video.html">This is a video embedded into html</a></li>
                <li><a href="audio.html">This is audio embedded into html</a></li>
            </ul>
        </article>
    </body>
</html>""" == comparison
