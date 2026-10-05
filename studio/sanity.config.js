// BluePrint content editor. Staff open it at https://<name>.sanity.studio
import {defineConfig} from 'sanity'
import {structureTool} from 'sanity/structure'
import {schemaTypes} from './schemaTypes'
import {PROJECT_ID, DATASET} from './project'

export default defineConfig({
  name: 'blueprint',
  title: 'BluePrint website',
  projectId: PROJECT_ID,
  dataset: DATASET,
  plugins: [
    structureTool({
      structure: (S) =>
        S.list()
          .title('Website content')
          .items([
            S.documentTypeListItem('post').title('Blog articles'),
            S.documentTypeListItem('vacancy').title('Job vacancies'),
          ]),
    }),
  ],
  schema: {types: schemaTypes},
})
