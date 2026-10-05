import {defineField, defineType} from 'sanity'
import {RtlInput} from '../components/Rtl'
import {richText} from './richText'

const ar = {components: {input: RtlInput}}

export default defineType({
  name: 'vacancy',
  title: 'Job vacancy',
  type: 'document',
  fieldsets: [
    {name: 'titles', title: 'Job title', options: {columns: 2}},
    {name: 'departments', title: 'Department (optional)', options: {columns: 2}},
    {name: 'locations', title: 'Location', options: {columns: 2}},
    {name: 'summaries', title: 'Short summary', options: {columns: 2}},
  ],
  fields: [
    defineField({name: 'status', title: 'Status', type: 'string', initialValue: 'open',
      description: 'Set to "Closed" to take the job off the website (it stays saved here).',
      options: {list: [{title: 'Open', value: 'open'}, {title: 'Closed', value: 'closed'}], layout: 'radio', direction: 'horizontal'},
      validation: (r) => r.required()}),
    defineField({name: 'titleEn', title: 'English', type: 'string', fieldset: 'titles', validation: (r) => r.required()}),
    defineField({name: 'titleAr', title: 'العربية', type: 'string', fieldset: 'titles', ...ar,
      validation: (r) => r.required().error('Please add the Arabic job title.')}),
    defineField({name: 'slug', title: 'Web address', type: 'slug', options: {source: 'titleEn', maxLength: 80},
      description: 'Click "Generate" after writing the English title.', validation: (r) => r.required()}),
    defineField({name: 'employmentType', title: 'Employment type', type: 'string', initialValue: 'Full time',
      options: {list: ['Full time', 'Part time', 'Contract', 'Internship'], layout: 'radio', direction: 'horizontal'}}),
    defineField({name: 'departmentEn', title: 'English', type: 'string', fieldset: 'departments'}),
    defineField({name: 'departmentAr', title: 'العربية', type: 'string', fieldset: 'departments', ...ar}),
    defineField({name: 'locationEn', title: 'English', type: 'string', fieldset: 'locations', initialValue: 'Riyadh, Saudi Arabia'}),
    defineField({name: 'locationAr', title: 'العربية', type: 'string', fieldset: 'locations', ...ar,
      initialValue: 'الرياض، المملكة العربية السعودية'}),
    defineField({name: 'datePosted', title: 'Date posted', type: 'date',
      initialValue: () => new Date().toISOString().slice(0, 10)}),
    defineField({name: 'closingDate', title: 'Closing date (optional)', type: 'date'}),
    defineField({name: 'summaryEn', title: 'English', type: 'text', rows: 3, fieldset: 'summaries', validation: (r) => r.required()}),
    defineField({name: 'summaryAr', title: 'العربية', type: 'text', rows: 3, fieldset: 'summaries', ...ar,
      validation: (r) => r.required().error('Please add the Arabic summary.')}),
    richText({name: 'descriptionEn', title: 'Full description (English)'}),
    richText({name: 'descriptionAr', title: 'الوصف الكامل (العربية)', arabic: true}),
  ],
  preview: {
    select: {title: 'titleEn', status: 'status', type: 'employmentType'},
    prepare: ({title, status, type}) => ({title, subtitle: (status === 'closed' ? 'Closed · ' : 'Open · ') + (type || '')}),
  },
})
