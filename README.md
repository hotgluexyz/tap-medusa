# tap-medusa

`tap-medusa` is a Singer tap for Medusa that produces JSON-formatted 
data following the [Singer spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md) 

## Configuration

### Accepted Config Options

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-medusa --about
```

### Configure using environment variables

This Singer tap will automatically import any environment variables within the working directory's
`.env` if the `--config=ENV` is provided, such that config values will be considered if a matching
environment variable is set either in the terminal context or in the `.env` file.

Sample config:
```$json
{
  "email": "email@email.com",
  "password": "******************",
  "base_url": "your_meda_url",
}
```

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

### Source Authentication and Authorization

## Usage

You can easily run `tap-medusa` by itself or in a pipeline.

### Executing the Tap Directly

```bash
tap-medusa --version
tap-medusa --help
tap-medusa --config CONFIG --discover > ./catalog.json
```

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

