// The article editor: paragraphs, headings, lists, quotes, bold/italic, links and pictures.
import {RtlInput} from '../components/Rtl'
import {defineArrayMember, defineField} from 'sanity'

export function richText({name, title, arabic = false, description}) {
  return defineField({
    name,
    title,
    description,
    type: 'array',
    ...(arabic ? {components: {input: RtlInput}} : {}),
    of: [
      defineArrayMember({
        type: 'block',
        styles: [
          {title: 'Paragraph', value: 'normal'},
          {title: 'Intro paragraph (larger)', value: 'lead'},
          {title: 'Heading', value: 'h2'},
          {title: 'Sub-heading', value: 'h3'},
          {title: 'Quote', value: 'blockquote'},
        ],
        lists: [
          {title: 'Bullets', value: 'bullet'},
          {title: 'Numbered', value: 'number'},
        ],
        marks: {
          decorators: [
            {title: 'Bold', value: 'strong'},
            {title: 'Italic', value: 'em'},
          ],
          annotations: [
            {
              name: 'link',
              type: 'object',
              title: 'Link',
              fields: [
                {
                  name: 'href',
                  type: 'url',
                  title: 'Address',
                  validation: (r) =>
                    r.uri({allowRelative: true, scheme: ['http', 'https', 'mailto', 'tel']}),
                },
              ],
            },
          ],
        },
      }),
      defineArrayMember({
        type: 'image',
        title: 'Picture',
        options: {hotspot: true},
        fields: [
          {name: 'alt', type: 'string', title: 'Short description (for blind visitors and Google)'},
          {name: 'caption', type: 'string', title: 'Caption (optional)'},
        ],
      }),
    ],
    validation: (r) => r.required().error(arabic ? 'Please write the Arabic article.' : 'Please write the article.'),
  })
}
