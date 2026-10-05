// Shows an Arabic field right-to-left while typing.
export function RtlInput(props) {
  return (
    <div dir="rtl" lang="ar" style={{fontFamily: "'IBM Plex Sans Arabic', 'Segoe UI', Tahoma, sans-serif"}}>
      {props.renderDefault(props)}
    </div>
  )
}
