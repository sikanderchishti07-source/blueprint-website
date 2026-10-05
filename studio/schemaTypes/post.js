import {defineField, defineType} from 'sanity'
import {RtlInput} from '../components/Rtl'
import {richText} from './richText'

// keep in step with CATEGORIES in build/sanity_source.py (that file holds the Arabic names)
const CATEGORIES = [
  'Permitting', 'Waste Permits', 'Renewals', 'Inspections', 'Quarries & Mining', 'Monitoring',
  'Reporting', 'Air Quality', 'Water', 'Marine', 'Climate & ESG', 'Regulatory update', 'Insight',
]
const ar = {components: {input: RtlInput}}

export default defineType({
  name: 'post',
  title: 'Blog article',
  type: 'document',
  fieldsets: [
    {name: 'titles', title: 'Title', options: {columns: 2}},
    {name: 'summaries', title: 'Short summary (shown on cards and in Google)', options: {columns: 2}},
  ],
  fields: [
    defineField({name: 'titleEn', title: 'English', type: 'string', fieldset: 'titles',
      validation: (r) => r.required().max(110)}),
    defineField({name: 'titleAr', title: 'العربية', type: 'string', fieldset: 'titles', ...ar,
      validation: (r) => r.required().error('Please add the Arabic title.')}),
    defineField({name: 'slug', title: 'Web address', type: 'slug',
      description: 'Click "Generate" after writing the English title. Do not change it after publishing.',
      options: {source: 'titleEn', maxLength: 80}, validation: (r) => r.required()}),
    defineField({name: 'publishedAt', title: 'Date', type: 'date',
      initialValue: () => new Date().toISOString().slice(0, 10), validation: (r) => r.required()}),
    defineField({name: 'category', title: 'Category', type: 'string',
      options: {list: CATEGORIES, layout: 'dropdown'}, initialValue: 'Insight', validation: (r) => r.required()}),
    defineField({name: 'coverImage', title: 'Cover picture', type: 'image', options: {hotspot: true},
      description: 'A wide photo works best (at least 1600 pixels wide).', validation: (r) => r.required()}),
    defineField({name: 'summaryEn', title: 'English', type: 'text', rows: 3, fieldset: 'summaries',
      validation: (r) => r.required().max(240)}),
    defineField({name: 'summaryAr', title: 'العربية', type: 'text', rows: 3, fieldset: 'summaries', ...ar,
      validation: (r) => r.required().error('Please add the Arabic summary.')}),
    richText({name: 'bodyEn', title: 'Article (English)'}),
    richText({name: 'bodyAr', title: 'المقال (العربية)', arabic: true}),
    defineField({name: 'actionRequired', title: 'Show an "Action required" badge', type: 'boolean', initialValue: false}),
    defineField({name: 'readingMinutes', title: 'Reading time in minutes (optional)', type: 'number',
      description: 'Leave empty and it is worked out from the article length.'}),
  ],
  orderings: [{title: 'Newest first', name: 'dateDesc', by: [{field: 'publishedAt', direction: 'desc'}]}],
  preview: {
    select: {title: 'titleEn', date: 'publishedAt', media: 'coverImage'},
    prepare: ({title, date, media}) => ({title, subtitle: date, media}),
  },
})
